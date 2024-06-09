document.addEventListener("DOMContentLoaded", function () {
  const searchWrapper = document.querySelector(".search-input");
  const inputBox = searchWrapper.querySelector("input");
  const suggBox = searchWrapper.querySelector(".autocom-box");
  const icon = searchWrapper.querySelector(".icon");

  const suggestions = [
    { symbol: "TSLA", name: "Tesla Inc." },
    { symbol: "AAPL", name: "Apple Inc." },
    { symbol: "MSFT", name: "Microsoft Corporation" },
    { symbol: "AMZN", name: "Amazon Inc." },
    { symbol: "SBI", name: "State Bank of India" },
    { symbol: "HDFCBANK", name: "HDFC Bank Ltd." },
    { symbol: "GOOGL", name: "Google Inc." },
    { symbol: "RIL", name: "Reliance Industries Limited" },
    { symbol: "TCS", name: "Tata Consultancy Services" },
    { symbol: "INFY", name: "Infosys Ltd." },
  ];

  inputBox.addEventListener("keyup", function (e) {
    let userData = e.target.value.trim();
    let emptyArray = [];

    if (userData) {
      emptyArray = suggestions.filter(data =>
        data.symbol.toLowerCase().startsWith(userData.toLowerCase()) ||
        data.name.toLowerCase().startsWith(userData.toLowerCase())
      ).map(data => `<li>${data.symbol} - ${data.name}</li>`);

      searchWrapper.classList.add("active");
      showSuggestions(emptyArray);
      handleSelection();
    } else {
      searchWrapper.classList.remove("active");
    }
  });

  function showSuggestions(list) {
    suggBox.innerHTML = list.length ? list.join('') : `<li>${inputBox.value.trim()}</li>`;
  }

  function handleSelection() {
    suggBox.querySelectorAll("li").forEach(item => {
      item.addEventListener("click", function () {
        let symbol = item.textContent.split(" - ")[0];
        let page = getPageForSymbol(symbol);
        if (page) {
          window.location.href = `${page}?symbol=${symbol}`;
        }
      });
    });
  }

  function getPageForSymbol(symbol) {
    switch (symbol) {
      case "TSLA":
        return "tsla2.html";
      case "AAPL":
        return "aapl2.html";
      case "INFY":
        return "infy2.html";
      case "MSFT":
        return "msft2.html";
      case "AMZN":
        return "amzn2.html";
      case "SBI":
        return "sbi2.html";
      case "HDFCBANK":
        return "hdfcbank2.html";
      case "GOOGL":
        return "googl2.html";
      case "RIL":
        return "reliance2.html";
      case "TCS":
        return "tcs2.html";

      default:
        return null; // No specific page found for the symbol
    }
  }

});
