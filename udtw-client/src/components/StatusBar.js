const colors = {
    'success': '#05668d',
    'warning': '#05668d',
    'error': '#bc4749',
}

function StatusBar({ type, text, leftText, rightText, height }) {
    height = height ?? 8;
    leftText = leftText ?? text;
    rightText = rightText ?? '';
    const color = colors[type] ?? '#bbb';

    return (
        <div 
            className={`flex justify-between items-center p-2 fixed bottom-0 left-0 w-full h-${height}`}
            style={{ background: color }}
        >
            <small className="text-white">{leftText}</small>
            <small className="text-white">{rightText}</small>
        </div>
    );
}

export default StatusBar;
