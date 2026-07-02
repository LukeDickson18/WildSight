function Navbar() {
  return (
    <nav className="border-b bg-white shadow-sm">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">
        <h1 className="text-2xl font-bold text-green-700">
          🌿 WildSight
        </h1>

        <div className="space-x-4">
          <button className="font-medium text-slate-600 hover:text-green-700">
            Login
          </button>

          <button className="rounded-lg bg-green-700 px-4 py-2 text-white transition hover:bg-green-800">
            Sign Up
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;