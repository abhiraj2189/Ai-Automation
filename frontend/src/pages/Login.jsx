import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { login } from "../api/authApi";

export default function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const data = await login(email, password);

      localStorage.setItem("token", data.access_token);

      alert("Login Successful ✅");

      navigate("/dashboard");

    } catch (err) {
      console.error(err);

      alert(
        err.response?.data?.detail || "Login Failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-zinc-950">

      <form
        onSubmit={handleLogin}
        className="bg-zinc-900 p-8 rounded-2xl w-[420px] shadow-xl"
      >

        <h1 className="text-3xl font-bold text-center mb-8">
          AI Automation Login
        </h1>

        <input
          className="w-full p-3 rounded bg-zinc-800 mb-4"
          placeholder="Email"
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
        />

        <input
          type="password"
          className="w-full p-3 rounded bg-zinc-800 mb-6"
          placeholder="Password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
        />

        <button
          disabled={loading}
          className="w-full bg-cyan-500 hover:bg-cyan-600 transition p-3 rounded-lg"
        >
          {loading ? "Logging in..." : "Login"}
        </button>

        <p className="text-center mt-6">

          Don't have an account?

          <Link
            to="/register"
            className="text-cyan-400 ml-2"
          >
            Register
          </Link>

        </p>

      </form>

    </div>
  );
}