function LoginPage() {
  return (
    <div className="flex min-h-[calc(100vh-80px)] items-center justify-center bg-slate-50 px-6">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">
        <h1 className="mb-2 text-center text-3xl font-bold text-slate-900">
          Welcome Back
        </h1>

        <p className="mb-8 text-center text-slate-600">
          Sign in to continue exploring WildSight.
        </p>

        <form className="space-y-6">
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
              placeholder="Enter your email"
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
              placeholder="Enter your password"
              className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-green-600"
            />
          </div>

          <button
            className="w-full rounded-lg bg-green-700 py-3 font-semibold text-white transition hover:bg-green-800"
          >
            Login
          </button>
        </form>

        <div className="mt-6 text-center">
          <button className="text-green-700 hover:underline">
            Forgot Password?
          </button>
        </div>

        <p className="mt-6 text-center text-slate-600">
          Don't have an account?{" "}
          <button className="font-semibold text-green-700 hover:underline">
            Sign Up
          </button>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;