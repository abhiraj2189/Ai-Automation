import MainLayout from "../layouts/MainLayout";

export default function Dashboard() {
  return (
    <MainLayout>

      <h1 className="text-4xl font-bold">
        Welcome Back 👋
      </h1>

      <p className="mt-3 text-zinc-400">
        AI Automation Dashboard
      </p>

      <div className="grid grid-cols-3 gap-6 mt-10">

        <div className="bg-zinc-900 rounded-xl p-6">
          <h2 className="text-xl font-bold">
            AI Chats
          </h2>

          <p className="text-4xl mt-4">
            0
          </p>
        </div>

        <div className="bg-zinc-900 rounded-xl p-6">
          <h2 className="text-xl font-bold">
            Notes
          </h2>

          <p className="text-4xl mt-4">
            0
          </p>
        </div>

        <div className="bg-zinc-900 rounded-xl p-6">
          <h2 className="text-xl font-bold">
            Favorites
          </h2>

          <p className="text-4xl mt-4">
            0
          </p>
        </div>

      </div>

    </MainLayout>
  );
}