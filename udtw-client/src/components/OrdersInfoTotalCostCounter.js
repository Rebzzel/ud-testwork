function OrdersInfoTotalCostCounter({ ordersInfo }) {
    const [totalCostInUsd, totalCostInRub] = ordersInfo.reduce((accumulator, orderInfo) => {
        return [ accumulator[0] + orderInfo.costInUsd, accumulator[1] + orderInfo.costInRub ];
    }, [ 0.0, 0.0 ]);

    return (
        <table className="border border-black">
            <thead>
                <tr className="h-12 bg-black text-white">
                    <th>Вся сумма</th>
                </tr>
            </thead>
            <tbody>
                <tr className="text-center text-2xl">
                    <td className="p-4">{totalCostInUsd} &#36; / {totalCostInRub} &#x20bd;</td>
                </tr>
            </tbody>
        </table>
    );
}

export default OrdersInfoTotalCostCounter;
