type SwitchProps = {
  label: string;
  checked: boolean;
  onChange: (checked: boolean) => void;
};

function Switch({
  label,
  checked,
  onChange,
}: SwitchProps) {
  return (
    <div className="flex items-center justify-between">
      <span className="font-medium text-slate-700">
        {label}
      </span>

      <button
        type="button"
        onClick={() => onChange(!checked)}
        className={`relative h-7 w-12 rounded-full transition-colors duration-200 ${
          checked
            ? "bg-green-700"
            : "bg-slate-300"
        }`}
      >
        <span
          className={`absolute top-1 h-5 w-5 rounded-full bg-white transition-transform duration-200 ${
            checked
              ? "translate-x-6"
              : "translate-x-1"
          }`}
        />
      </button>
    </div>
  );
}

export default Switch;