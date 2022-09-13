import { SpinnerCircular } from 'spinners-react';

const Loader = ({ status }) => {
    return (
        <div className="fixed top-0 left-0 w-full h-full bg-[#f3f3f3f3]">
            <div className="absolute top-1/2 left-1/2">
                <div className="flex flex-col items-center translate-x-[-50%] translate-y-[-50%]">
                    <SpinnerCircular/>
                    <label className="text-slate-500">{status}</label>
                </div>
            </div>
        </div>
    );
};

export default Loader;
