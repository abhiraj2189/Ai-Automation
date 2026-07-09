export default function Navbar() {
  return (
    <header className="h-16 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-6">
      <h1 className="text-xl font-bold">
        AI Automation Dashboard
      </h1>

      <div className="flex items-center gap-4">
        <span className="text-gray-400">
          Welcome, Abhiraj 👋
        </span>
      </div>
    </header>
  );
}