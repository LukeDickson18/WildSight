import { Link } from "react-router-dom";

import AuthLayout from "../layouts/AuthLayout";
import Button from "../components/ui/Button";
import Card from "../components/ui/Card";

function NotFoundPage() {
  return (
    <AuthLayout>
      <Card className="w-full max-w-md text-center">
        <h1 className="text-7xl font-bold text-green-700">
          404
        </h1>

        <h2 className="mt-4 text-3xl font-semibold text-slate-900">
          Page Not Found
        </h2>

        <p className="mt-4 text-slate-600">
          Sorry, the page you're looking for doesn't exist or has been moved.
        </p>

        <Link to="/">
          <Button className="mt-8 w-full">
            Return Home
          </Button>
        </Link>
      </Card>
    </AuthLayout>
  );
}

export default NotFoundPage;