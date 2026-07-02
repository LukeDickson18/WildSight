import type { InputHTMLAttributes } from "react";

type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label: string;
};

function Input({
  label,
  id,
  className = "",
  ...props
}: InputProps) {
  return (
    <div>
      <label
        htmlFor={id}
        className="mb-2 block font-medium text-slate-700"
      >
        {label}
      </label>

      <input
        id={id}
        className={`w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-green-600 ${className}`}
        {...props}
      />
    </div>
  );
}

export default Input;