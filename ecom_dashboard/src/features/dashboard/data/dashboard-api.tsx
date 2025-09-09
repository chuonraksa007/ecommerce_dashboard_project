const DASHBOARD_URL = "http://127.0.0.1:8001/ecoms/dashboard";

async function fetchDashboard() {
  try {
    const res = await fetch(DASHBOARD_URL, {
      next: { revalidate: 60 }, // optional: Next.js caching
    });

    if (!res.ok) {
      throw new Error(`Failed to fetch: ${res.status}`);
    }

    const json = await res.json();
    return json.data || {};
  } catch (err) {
    console.error("Error fetching dashboard:", err);
    return {};
  }
}

export async function fetchMetrics() {
  const data = await fetchDashboard();
  return data.metrics_card || [];
}

export async function fetchSaleOverview() {
  const data = await fetchDashboard();
  return data.sale_overview || [];
}

export async function fetchTopSellingProducts() {
  const data = await fetchDashboard();
  return data.top_products || [];
}

export async function fetchRecentOrders() {
  const data = await fetchDashboard();
  return data.recent_order || [];
}
