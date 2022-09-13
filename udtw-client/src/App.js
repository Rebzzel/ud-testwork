import axios from 'axios';
import getObjectHash from 'object-hash';
import { useState, useEffect } from 'react';

import './App.css';

import OrderInfo from './models/OrderInfo.js';

import OrdersInfoChart from './components/OrdersInfoChart.js';
import OrdersInfoTable from './components/OrdersInfoTable.js';
import OrdersInfoTotalCostCounter from './components/OrdersInfoTotalCostCounter.js';
import StatusBar from './components/StatusBar.js';

const API_URL = process.env.REACT_APP_API_URL ?? 'http://localhost:5000';
const TARGET_ID = process.env.REACT_APP_TARGET_ID ?? '1DwfUKQ1jbBkMW-dPr1jRsYY-SifQDwUKqscXr67lCPk';
const ENDPOINT_URL = (new URL(`/handle/spreadsheet/${TARGET_ID}`, API_URL)).href;
const UPDATE_INTERVAL = process.env.REACT_APP_UPDATE_INTERVAL_IN_MS ?? 1000;

// NOTE: Constants prevent us from useless updates.
const SUCCESS_STATUS = { type: 'success', text: 'Success' };
const FETCHING_DATA_STATUS = { type: 'warning', text: 'Fetching data' };
const SERVER_NOT_RESPONDING_STATUS = { type: 'error', text: 'Server is not responding' };
const NOTHING_TO_UPDATE_STATUS = { type: 'success', text: 'Nothing to update' };

function App() {
    const [ordersInfo, setOrdersInfo] = useState({
        data: [],
        hash: null,
    });

    const [status, setStatus] = useState(FETCHING_DATA_STATUS);

    useEffect(() => {
        const requestUpdate = async () => {
            try {
                var {data, hash} = await fetchOrdersInfo(ordersInfo.hash);
            } catch (error) {
                setStatus(SERVER_NOT_RESPONDING_STATUS);
                throw error;
            }

            if (hash !== ordersInfo.hash) {
                setOrdersInfo({ data, hash });
                setStatus(SUCCESS_STATUS);
            } else {
                setStatus(NOTHING_TO_UPDATE_STATUS);
            }
        };

        let lastRequestTimerId = null;
        
        const requestUpdateLoop = () => {
            lastRequestTimerId = setTimeout(() => {
                requestUpdate().finally(() => requestUpdateLoop());
            }, UPDATE_INTERVAL);
        };
        
        requestUpdateLoop();

        return () => clearTimeout(lastRequestTimerId);
   }, [ordersInfo]);

    return (
        <div>
            <div className="m-2 xl:flex">
                <div className="xl:w-1/2 flex flex-col items-center">
                    <OrdersInfoChart ordersInfo={ordersInfo.data}/>
                </div>
                <div className="xl:w-1/2 flex flex-col items-center space-y-4">
                    <OrdersInfoTotalCostCounter ordersInfo={ordersInfo.data}/>
                    <OrdersInfoTable ordersInfo={ordersInfo.data}/>
                </div>
            </div>
            { status.text && <StatusBar text={status.text} type={status.type}/> }
        </div>
    );
}

async function fetchOrdersInfo(oldHash) {
    const response = await axios.get(ENDPOINT_URL);
    console.log(response);

    const hash = getObjectHash(response.data);

    if (hash === oldHash) {
        return { data: [], hash };
    }

    const ordersInfo = [];

    for (const entry of response.data) {
        ordersInfo.push(new OrderInfo(
            entry['id'],
            entry['order_id'],
            entry['cost_in_usd'],
            entry['cost_in_rub'],
            entry['delivery_at'],
        ));
    }

    return { data: ordersInfo, hash };
}

export default App;
