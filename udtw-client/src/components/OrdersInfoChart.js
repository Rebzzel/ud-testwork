import Chart from 'react-apexcharts';

const OrdersInfoChart = ({ ordersInfo }) => {
    const actualOrdersInfo = ordersInfo;

    return (
        <Chart
            type="line"
            options={{
                stroke: {
                    width: [1, 0, 0]
                },
                xaxis: {
                    categories: actualOrdersInfo.map(info => info.deliveryAt)
                },
                yaxis: {
                    tickAmount: 3,
                    max: 6000,
                    min: 0,
                }
            }}
            series={[
                {
                    name: '',
                    type: 'line',
                    data: actualOrdersInfo.map(info => info.costInUsd),
                }
            ]}
            width="800"
        />
    );
};

export default OrdersInfoChart;
