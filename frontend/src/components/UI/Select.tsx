import type { SelectHTMLAttributes } from "react";

type Option = {
  value: string;
  label: string;
};

type SelectProps = SelectHTMLAttributes<HTMLSelectElement> & {
  label: string;
  options: Option[];
};

function Select({
  label,
  id,
  options,
  className = "",
  ...props
}: SelectProps) {
  return (
    <div>
      <label
        htmlFor={id}
        className="mb-2 block font-medium text-slate-700"
      >
        {label}
      </label>

      <select
        id={id}
        className={`w-full rounded-lg border border-slate-300 bg-white px-4 py-3 outline-none transition focus:border-green-600 ${className}`}
        {...props}
      >
        {options.map((option) => (
          <option
            key={option.value}
            value={option.value}
          >
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}

export default Select;