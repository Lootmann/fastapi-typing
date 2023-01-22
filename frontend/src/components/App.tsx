import React from "react";
import { Problems } from "./Problems";
import { Records } from "./Records";

import "../styles/layout.css";

export function App() {
  return (
    <div className="app">
      <Problems />
      <Records />
    </div>
  );
}
