import React from "react";
import Dashboard from "./components/Dashboard";
import ThreatMap from "./components/ThreatMap";
import Analytics from "./components/Analytics";
import ScanInterface from "./components/ScanInterface";
import ReportBuilder from "./components/ReportBuilder";
import RealTimeMonitor from "./components/RealTimeMonitor";

export default function App(): JSX.Element {
  return (
    <main>
      <h1>Advanced Enterprise Web Vulnerability Platform</h1>
      <Dashboard />
      <ThreatMap />
      <Analytics />
      <ScanInterface />
      <ReportBuilder />
      <RealTimeMonitor />
    </main>
  );
}
