export default function Navbar() {
  return (
    <header className="h-16 bg-zinc-900 border-b border-zinc-800 flex items-center justify-between px-6">
      <div>
        <h1 className="text-2xl font-bold text-cyan-400">
          AI Automation
        </h1>
      </div>

      <div className="flex items-center gap-4">
        <span className="text-zinc-400">
          Welcome 👋
        </span>
      </div>
    </header>
  );
}