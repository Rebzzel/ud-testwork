import { Table, Thead, Tbody, Tr, Th } from 'react-super-responsive-table';
import 'react-super-responsive-table/dist/SuperResponsiveTableStyle.css';
import OrderInfoTableEntry from './OrderInfoTableEntry.js';

const OrdersInfoTable = ({ ordersInfo }) => {
    return (
        <Table>
            <Thead className="sm:h-12 bg-black text-white">
                <Tr className="table table-fixed w-full h-full">
                    <Th>№</Th>
                    <Th>Заказ №</Th>
                    <Th>Стоимость</Th>
                    <Th>Срок поставки</Th>
                </Tr>
            </Thead>
            <Tbody className="block h-[600px] overflow-auto border border-black">
                { 
                    ordersInfo.map((orderInfo) => 
                        <OrderInfoTableEntry 
                            key={orderInfo.id.toString()}
                            {...orderInfo}
                        />
                    )
                }
            </Tbody>
        </Table>
    );
};

export default OrdersInfoTable;
