function RegisterPage() {
  return (
    <div className="flex min-h-[calc(100vh-80px)] items-center justify-center bg-slate-50 px-6 py-12">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">
        <h1 className="mb-2 text-center text-3xl font-bold text-slate-900">
          Create an Account
        </h1>

        <p className="mb-8 text-center text-slate-600">
          Join WildSight and start recording your wildlife observations.
        </p>

        <form className="space-y-5">
          <div>
            <label
              htmlFor="name"
              className="mb-2 block font-medium text-slate-700"
            >
              Full Name
            </label>

            <input
              id="name"
              type="text"
              placeholder="John Smith"
              className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-green-600"
            />
          </div>

          <div>
            <label
              htmlFor="email"
              className="mb-2 block font-medium text-slate-700"
            >
              Email
            </label>

            <input
              id="email"
              type="email"
              placeholder="john@example.com"
              className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-green-600"
            />
          </div>

          <div>
            <label
              htmlFor="password"
              className="mb-2 block font-medium text-slate-700"
            >
              Password
            </label>

            <input
              id="password"
              type="password"
              placeholder="Create a password"
              className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-green-600"
            />
          </div>

          <div>
            <label
              htmlFor="confirmPassword"
              className="mb-2 block font-medium text-slate-700"
            >
              Confirm Password
            </label>

            <input
              id="confirmPassword"
              type="password"
              placeholder="Confirm your password"
              className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-green-600"
            />
          </div>

          <button className="w-full rounded-lg bg-green-700 py-3 font-semibold text-white transition hover:bg-green-800">
            Create Account
          </button>
        </form>

        <p className="mt-6 text-center text-slate-600">
          Already have an account?{" "}
          <button className="font-semibold text-green-700 hover:underline">
            Login
          </button>
        </p>
      </div>
    </div>
  );
}

export default RegisterPage;