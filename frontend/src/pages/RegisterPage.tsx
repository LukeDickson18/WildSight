import AuthLayout from "../layouts/AuthLayout";

import Card from "../components/ui/Card";
import Button from "../components/ui/Button";
import Input from "../components/ui/Input";

function RegisterPage() {
  return (
    <AuthLayout>
      <Card className="w-full max-w-md">
        <h1 className="mb-2 text-center text-3xl font-bold text-slate-900">
          Create an Account
        </h1>

        <p className="mb-8 text-center text-slate-600">
          Join WildSight and start recording your wildlife observations.
        </p>

        <form className="space-y-5">
          <Input
            id="name"
            label="Full Name"
            placeholder="John Smith"
          />

          <Input
            id="email"
            label="Email"
            type="email"
            placeholder="john@example.com"
          />

          <Input
            id="password"
            label="Password"
            type="password"
            placeholder="Create a password"
          />

          <Input
            id="confirmPassword"
            label="Confirm Password"
            type="password"
            placeholder="Confirm your password"
          />

          <Button className="w-full">
            Create Account
          </Button>
        </form>

        <p className="mt-6 text-center text-slate-600">
          Already have an account?{" "}
          <button className="font-semibold text-green-700 hover:underline">
            Login
          </button>
        </p>
      </Card>
    </AuthLayout>
  );
}

export default RegisterPage;