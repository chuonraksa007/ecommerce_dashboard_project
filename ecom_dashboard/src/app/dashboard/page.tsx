import { AppSidebar } from "@/shared/components/app-sidebar"
import { SiteHeader } from "@/shared/components/site-header"
import MetricsCard from "@/features/dashboard/components/metrics-card-component"
import SaleOverview from "@/features/dashboard/components/sale-overview-component"
import TopSellingProduct from "@/features/dashboard/components/top-selling-component"
import RecentOrder from "@/features/dashboard/components/recent-order"

import {
  SidebarInset,
  SidebarProvider,
} from "@/shared/components/ui/sidebar"

export default function Page() {
  return (
    <SidebarProvider
      style={
        {
          "--sidebar-width": "calc(var(--spacing) * 72)",
          "--header-height": "calc(var(--spacing) * 12)",
        } as React.CSSProperties
      }
    >
      <AppSidebar variant="inset" />
      <SidebarInset>
        <SiteHeader />
       <div className="flex flex-1 flex-col pt-0 gap-8 lg:pt-4 lg:pb-6 lg:px-8">  
          <MetricsCard />

          {/* Two-column layout */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-0">
            {/* Left column */}
            <SaleOverview />

            {/* Right column */}
            <TopSellingProduct />
          </div>

          <RecentOrder />
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}
