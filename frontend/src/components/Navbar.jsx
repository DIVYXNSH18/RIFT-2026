import React from 'react';

const PipelineIcon = ({ size = 24, color = "#fff" }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    stroke={color}
    strokeWidth="2"
    strokeLinecap="round"
  >
    <circle cx="6" cy="6" r="3" />
    <circle cx="18" cy="18" r="3" />
    <circle cx="18" cy="6" r="3" />
    <line x1="6" y1="9" x2="6" y2="15" />
    <line x1="9" y1="6" x2="15" y2="6" />
    <line x1="6" y1="15" x2="18" y2="15" />
  </svg>
);

const Navbar = ({ activePage, setActivePage }) => {
  const tabs = ["analyze", "results", "score", "timeline"];
  const labels = {
    analyze: "Analyze",
    results: "Results",
    score: "Score",
    timeline: "Timeline",
  };

  return (
    <nav
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        right: 0,
        height: 64,
        zIndex: 100,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 32px",
        backdropFilter: "blur(20px)",
        WebkitBackdropFilter: "blur(20px)",
        background: "rgba(255,255,255,0.88)",
        borderBottom: "1px solid #e8e7e3",
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        <div
          style={{
            width: 36,
            height: 36,
            background: "#2a2926",
            borderRadius: 8,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <PipelineIcon size={20} />
        </div>
        <div>
          <div
            style={{
              fontFamily: "'Playfair Display', serif",
              fontSize: 18,
              fontWeight: 700,
              color: "#111110",
              lineHeight: 1.1,
            }}
          >
            PipelineIQ
          </div>
          <div
            style={{
              fontFamily: "'DM Sans', sans-serif",
              fontSize: 11,
              color: "#6b6860",
              fontWeight: 300,
            }}
          >
            by RIFT ORGANISERS
          </div>
        </div>
      </div>

      <div
        className="nav-tabs"
        style={{
          display: "flex",
          gap: 6,
          background: "#f2f1ee",
          borderRadius: 20,
          padding: "4px",
        }}
      >
        {tabs.map((tab) => (
          <button
            key={tab}
            onClick={() => setActivePage(tab)}
            style={{
              padding: "6px 18px",
              borderRadius: 16,
              fontFamily: "'DM Sans', sans-serif",
              fontSize: 14,
              fontWeight: activePage === tab ? 600 : 400,
              background: activePage === tab ? "#2a2926" : "transparent",
              color: activePage === tab ? "#fff" : "#6b6860",
              transition: "all 0.2s ease",
              border: "none",
            }}
          >
            <span>{labels[tab]}</span>
          </button>
        ))}
      </div>

      <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <span
            style={{
              width: 8,
              height: 8,
              background: "#14784a",
              borderRadius: "50%",
              animation: "dotPulse 2s ease infinite",
              display: "inline-block",
            }}
          />
          <span
            style={{
              fontFamily: "'DM Mono', monospace",
              fontSize: 12,
              color: "#2a2926",
              fontWeight: 500,
            }}
          >
            Agent Ready
          </span>
        </div>
        <button
          onClick={() => alert('Login functionality coming soon!')}
          style={{
            padding: "8px 20px",
            background: "#2a2926",
            color: "#fff",
            borderRadius: 8,
            fontFamily: "'DM Sans', sans-serif",
            fontSize: 14,
            fontWeight: 500,
            transition: "all 0.2s ease",
            border: "none",
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.background = "#111110";
            e.currentTarget.style.transform = "translateY(-1px)";
            e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.15)";
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.background = "#2a2926";
            e.currentTarget.style.transform = "translateY(0)";
            e.currentTarget.style.boxShadow = "none";
          }}
        >
          Login
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
