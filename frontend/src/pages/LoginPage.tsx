import AuthLayout from "../layouts/AuthLayout";

import Card from "../components/ui/Card";
import Button from "../components/ui/Button";
import Input from "../components/ui/Input";

function LoginPage() {
  return (
    <AuthLayout>
      <Card className="w-full max-w-md">
        <h1 className="mb-2 text-center text-3xl font-bold text-slate-900">
          Welcome Back
        </h1>

        <p className="mb-8 text-center text-slate-600">
          Sign in to continue exploring WildSight.
        </p>

        <form className="space-y-5">
          <Input
            id="email"
            label="Email"
            type="email"
            placeholder="Enter your email"
          />

          <Input
            id="password"
            label="Password"
            type="password"
            placeholder="Enter your password"
          />

          <Button className="w-full">
            Login
          </Button>
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
      </Card>
    </AuthLayout>
  );
}

export default LoginPage;