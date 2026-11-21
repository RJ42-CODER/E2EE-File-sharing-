import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Connecting to backend...");
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Backend request failed");
        }
        return response.json();
      })
      .then((data) => {
        setMessage(data.message);
      })
      .catch((error) => {
        setError("Could not connect to backend");
      });
  }, []);

  return (
    <main>
      <h1>E2EE Secure File Sharing</h1>
      <h2>Backend Connection</h2>
      {/* ternary operator to display error or message */}
      {error ? <p>{error}</p> : <p>{message}</p>}
    </main>
  );
}

export default App;
