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
/* -------------------------------------------------------------------------- */
function handleError(message, source, lineno, colno, error) {
  const toastElement = document.createElement("div");
  toastElement.classList.add(
    "toast",
    "show",
    "bg-glass",
    "text-light",
    "position-fixed", // Changed from "position-absolute"
    "top-0", // Positioned at the top
    "start-0", // Positioned at the right
    "m-3",
    "rounded-3",
    "p-3",
    "fade",
    "text-textcolor"
  );
  toastElement.setAttribute("role", "alert");
  toastElement.setAttribute("aria-live", "assertive");
  toastElement.innerHTML = `
  <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      <div class="toast-body text-center almarai-bold text-redalert">
        حدث خطأ
      </div>
  `;

  document.body.appendChild(toastElement);
  const toast = new bootstrap.Toast(toastElement);
  toast.show();
}
export function withErrorHandler(fn) {
  return async (...args) => {
    try {
      return await fn(...args);
    } catch (error) {
      console.error(error);
      handleError(
        error.message,
        error.source,
        error.lineno,
        error.colno,
        error
      );
    }
  };
}

// in some cases while designing the page, you want to jump
// to specific element when page loads
export function jumpToElement(elementId) {
  /**
   * @param {string} elementId
   * @returns {void}
   * here is an example of how to use it
   * at the end of your template file add this
   * ''' html
   * <script type="module">import {jumpToElement} from "{% static 'js' %}/utils.js";
   *   jumpToElement("jumpOnLoad");
   * </script>
   * '''
   */
  const element = document.querySelector(`#${elementId}`);
  element.scrollIntoView({ behavior: "smooth" });
}
