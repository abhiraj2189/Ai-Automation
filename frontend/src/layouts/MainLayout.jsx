import Sidebar from "../components/sidebar/Sidebar";
import Navbar from "../components/navbar/Navbar";

export default function MainLayout({ children }) {
  return (
    <div className="flex min-h-screen bg-zinc-950 text-white">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Navbar />

        <main className="p-8">
          {children}
        </main>

      </div>

    </div>
  );
}