import React from "react";
import { Problems } from "./Problems";
import { Records } from "./Records";

export function App() {
  return (
    <div className="h-screen w-screen p-3 bg-gray-800 text-slate-100 flex flex-col gap-5">
      <h1 className="text-3xl font-bold underline">Typing Game</h1>
      <Problems />
      <Records />
    </div>
  );
}
