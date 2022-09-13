import { Tr, Td as BaseTd } from 'react-super-responsive-table';

const Td = props => <BaseTd className="border-r border-slate-300" {...props}/>

const OrderInfo = ({id, orderId, costInUsd, costInRub, deliveryAt}) => {
    return (
        <Tr className="table table-fixed w-full sm:h-8 border-b border-slate-300">
            <Td>{id}</Td>
            <Td>{orderId}</Td>
            <Td>{costInUsd} $ ({costInRub} ₽)</Td>
            <Td>{deliveryAt}</Td>
        </Tr>
    );
};

export default OrderInfo;
