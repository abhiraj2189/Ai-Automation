export default function Navbar() {
  return (
    <header className="h-20 border-b border-zinc-800 bg-zinc-900 flex items-center justify-between px-8">

      <h2 className="text-2xl font-bold">
        Dashboard
      </h2>

      <div className="flex items-center gap-4">

        <img
          src="https://i.pravatar.cc/40"
          className="rounded-full"
          alt="profile"
        />

      </div>

    </header>
  );
}