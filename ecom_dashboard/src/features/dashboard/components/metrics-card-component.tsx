'use client';

import { useEffect, useState } from 'react';
import { fetchMetrics } from '@/features/dashboard/data/dashboard-api';
import { Badge } from '@/shared/components/ui/badge';
import { Button } from '@/shared/components/ui/button';
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardToolbar,
} from '@/shared/components/ui/card';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/shared/components/ui/dropdown-menu';
import {
  ArrowDown,
  ArrowUp,
  MoreHorizontal,
  Pin,
  Settings,
  Share2,
  Trash,
  TriangleAlert,
} from 'lucide-react';

function formatNumber(n: string) {
  return n; // API already sends formatted values like "$143"
}

export default function MetricsCard() {
  const [metrics, setMetrics] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const data = await fetchMetrics();
      setMetrics(data);
      setLoading(false);
    }
    load();
  }, []);

  if (loading) {
    return <p className="text-muted-foreground text-sm">Loading...</p>;
  }

  return (
    <div className="pt-0">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {metrics.map((metric, index) => (
          <Card key={index}>
            <CardHeader className="border-0">
              <CardTitle className="text-muted-foreground text-sm font-medium">
                {metric.title}
              </CardTitle>
              <CardToolbar>
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <Button
                      variant="dim"
                      size="sm"
                      mode="icon"
                      className="-me-1.5"
                    >
                      <MoreHorizontal />
                    </Button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent align="end" side="bottom">
                    <DropdownMenuItem>
                      <Settings />
                      Settings
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                      <TriangleAlert /> Add Alert
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                      <Pin /> Pin to Dashboard
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                      <Share2 /> Share
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem variant="destructive">
                      <Trash />
                      Remove
                    </DropdownMenuItem>
                  </DropdownMenuContent>
                </DropdownMenu>
              </CardToolbar>
            </CardHeader>
            <CardContent className="space-y-2.5">
              <div className="flex items-center gap-2.5">
                <span className="text-2xl font-medium text-foreground tracking-tight">
                  {formatNumber(metric.value)}
                </span>
                <Badge
                  variant={metric.isPositive ? 'success' : 'destructive'}
                  appearance="light"
                >
                  {metric.isPositive ? <ArrowUp /> : <ArrowDown />}
                  {metric.change}
                </Badge>
              </div>
              <div className="text-xs text-muted-foreground mt-2 border-t pt-2.5">
                {metric.changeLabel}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
