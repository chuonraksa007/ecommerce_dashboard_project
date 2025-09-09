import { AppSidebar } from "@/shared/components/app-sidebar"
import { SiteHeader } from "@/shared/components/site-header"
import { AnalyticPage } from "@/features/analytic/components/analyticComponent"

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
         <AnalyticPage />
        </div>
      </SidebarInset>
    </SidebarProvider>
  )
}
