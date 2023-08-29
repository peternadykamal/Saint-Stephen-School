/* ---------------------------- toggle visibility --------------------------- */
export function toggleVisibility(targetClassName, parentId) {
  const parentElement = document.querySelector(`#${parentId}`);
  const directChildren = parentElement.children;

  for (const child of directChildren) {
    // Check if the element has the target class
    const hasTargetClass = child.classList.contains(targetClassName);

    // Remove or add the 'd-none' class based on whether it's the target class
    if (hasTargetClass) {
      child.classList.remove("d-none");
    } else {
      child.classList.add("d-none");
    }
  }
}
// toggleVisibility("editTagSpinner", "addEditTag");
export function elementVisibility(isVisible, querySelectorValue) {
  const elements = document.querySelectorAll(querySelectorValue);
  elements.forEach((element) => {
    if (!isVisible) {
      element.classList.add("d-none");
    } else {
      element.classList.remove("d-none");
    }
  });
}
// elementVisibility(false, "#school_level_year_container");
/* ----------------------------- sleep function ----------------------------- */
export const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
/* ----------------------------- get api url ----------------------------- */
export function getApiUrl(path) {
  const protocol = window.location.protocol;
  const hostname = window.location.hostname;
  const port = window.location.port;

  let apiUrl;
  if (!isNaN(port) && port !== "") {
    apiUrl = `${protocol}//${hostname}:${port}${path}`;
  } else {
    apiUrl = `${protocol}//${hostname}${path}`;
  }

  return apiUrl;
}
/* ----------------------------- get csrf token ----------------------------- */
export function getCSRFToken() {
  const cookieValue = document.cookie
    .split("; ")
    .find((cookie) => cookie.startsWith("csrftoken="))
    .split("=")[1];

  return cookieValue;
}
/* ----------------------- make a get or post request ----------------------- */
export async function makeRequest(method, url, data = {}) {
  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
  };

  if (method === "POST") {
    options.body = JSON.stringify(data);
  }
  const fullUrl = getApiUrl(url);
  const response = await fetch(fullUrl, options);
  const json = await response.json();
  return json;
}
// makeRequest("GET", "/api/tags/");
// makeRequest("POST", "/api/tags/", { name: "new tag" });
