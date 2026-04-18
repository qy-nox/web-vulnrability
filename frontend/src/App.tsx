import React from "react";
import ScannerInterface from "./components/ScannerInterface";
import VulnerabilityDisplay, { type VulnerabilityItem } from "./components/VulnerabilityDisplay";
import ReportGenerator from "./components/ReportGenerator";
import "./styles.css";

export default function App(): JSX.Element {
  const [progress, setProgress] = React.useState(0);
  const [scanId, setScanId] = React.useState("");
  const [vulnerabilities, setVulnerabilities] = React.useState<VulnerabilityItem[]>([]);

  const handleScanStarted = (id: string): void => {
    setProgress(15);
    setScanId(id);
  };

  const handleProgress = (value: number): void => {
    setProgress(Math.max(0, Math.min(100, value)));
  };

  const handleVulnerabilitiesLoaded = (items: VulnerabilityItem[]): void => {
    setVulnerabilities(items);
    setProgress(100);
  };

  return (
    <main className="container">
      <h1>Web Vulnerability Scanner</h1>
      <p className="subtle">Run 3000+ checks and review findings by severity, type, and confidence.</p>
      <ScannerInterface
        progress={progress}
        onScanStarted={handleScanStarted}
        onProgress={handleProgress}
        onVulnerabilitiesLoaded={handleVulnerabilitiesLoaded}
      />
      <VulnerabilityDisplay scanId={scanId} vulnerabilities={vulnerabilities} />
      <ReportGenerator scanId={scanId} vulnerabilities={vulnerabilities} />
    </main>
  );
}
