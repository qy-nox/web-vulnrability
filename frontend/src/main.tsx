import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

const target = document.getElementById("root");
if (target) {
  createRoot(target).render(<App />);
}
