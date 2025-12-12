import { cn } from "@/lib/utils";

interface RadioSwitchProps {
  name: string;
  options: number[];
  value: number;
  onChange: (value: number) => void;
}

const RadioSwitch = ({ name, options, value, onChange }: RadioSwitchProps) => {
  return (
    <div className="radio-switch">
      {options.map((option, index) => (
        <label
          key={option}
          className={cn(
            "radio-switch-item",
            value === option && "active"
          )}
        >
          <input
            type="radio"
            name={name}
            value={option}
            checked={value === option}
            onChange={() => onChange(option)}
            className="sr-only"
          />
          {option}
        </label>
      ))}
    </div>
  );
};

export default RadioSwitch;
