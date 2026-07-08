type Props = {
  onClick: () => void;
};

function FindMeButton({ onClick }: Props) {
  return (
    <button
      onClick={onClick}
      className="rounded-lg bg-emerald-600 px-4 py-2 text-white hover:bg-emerald-700"
    >
      📍 Find Me
    </button>
  );
}

export default FindMeButton;