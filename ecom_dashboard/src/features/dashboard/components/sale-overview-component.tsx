'use client';

import React, { useEffect, useState } from 'react';
import { Badge } from '@/shared/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/shared/components/ui/card';
import { ChartConfig, ChartContainer, ChartTooltip } from '@/shared/components/ui/chart';
import { TrendingUp } from 'lucide-react';
import { Area, CartesianGrid, ComposedChart, Line, XAxis, YAxis } from 'recharts';
import { fetchSaleOverview } from '@/features/dashboard/data/dashboard-api';

// Chart configuration
const chartConfig = {
  value: {
    label: 'Sales',
    color: 'var(--color-violet-500) ',
  },
} satisfies ChartConfig;

// Custom Tooltip
interface TooltipProps {
  active?: boolean;
  payload?: Array<{
    dataKey: string;
    value: number;
    color: string;
  }>;
  label?: string;
}

const CustomTooltip = ({ active, payload }: TooltipProps) => {
  if (active && payload && payload.length) {
    return (
      <div className="rounded-lg bg-zinc-900 text-white p-3 shadow-lg">
        <div className="text-xs font-medium mb-1">Total:</div>
        <div className="text-sm font-semibold">${payload[0].value.toLocaleString()}</div>
      </div>
    );
  }
  return null;
};

export default function SaleOverview() {
  const [data, setData] = useState<{ month: string; value: number }[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const apiResponse = await fetchSaleOverview();

        // Map API -> chart format {month, value}
        const normalized = (apiResponse || []).map((item: any) => ({
          month: item.month,
          value: item.sales, // use sales instead of value
        }));

        setData(normalized);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  if (loading) {
    return <div className="p-6">Loading chart...</div>;
  }

  // Calculate stats
  const totalSales = data.reduce((sum, item) => sum + item.value, 0);
  const lastValue = data[data.length - 1]?.value || 0;
  const previousValue = data[data.length - 2]?.value || 0;
  const percentageChange = previousValue > 0 ? ((lastValue - previousValue) / previousValue) * 100 : 0;

  return (
    <div className="pt-0">
      <Card className="w-full lg:max-w-4xl">
        <CardHeader className="border-0 min-h-auto pt-6 pb-4">
          <CardTitle className="text-lg font-semibold">Sale Overview</CardTitle>
        </CardHeader>

        <CardContent className="px-0">
          {/* Stats Section */}
          <div className="px-5 mb-8">
            <div className="flex items-center gap-3 mb-4">
              <div className="text-3xl font-bold">${totalSales.toLocaleString()}</div>
              <Badge variant="success" appearance="light">
                <TrendingUp className="size-3" />
                {Math.abs(percentageChange).toFixed(2)}%
              </Badge>
            </div>
          </div>

          {/* Chart */}
          <div className="relative">
            <ChartContainer
              config={chartConfig}
              className="h-[300px] w-full ps-1.5 pe-2.5 overflow-visible [&_.recharts-curve.recharts-tooltip-cursor]:stroke-initial"
            >
              <ComposedChart
                data={data}
                margin={{
                  top: 25,
                  right: 25,
                  left: 0,
                  bottom: 25,
                }}
                style={{ overflow: 'visible' }}
              >
                {/* Gradient */}
                <defs>
                  <linearGradient id="salesGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor={chartConfig.value.color} stopOpacity={0.15} />
                    <stop offset="100%" stopColor={chartConfig.value.color} stopOpacity={0} />
                  </linearGradient>
                  <filter id="dotShadow" x="-50%" y="-50%" width="200%" height="200%">
                    <feDropShadow dx="2" dy="2" stdDeviation="3" floodColor="rgba(0,0,0,0.5)" />
                  </filter>
                </defs>

                <CartesianGrid
                  strokeDasharray="4 12"
                  stroke="var(--input)"
                  strokeOpacity={1}
                  horizontal={true}
                  vertical={false}
                />

                <XAxis
                  dataKey="month"
                  axisLine={false}
                  tickLine={false}
                  tick={{ fontSize: 12 }}
                  tickMargin={12}
                  dy={10}
                />

                <YAxis
                  axisLine={false}
                  tickLine={false}
                  tick={{ fontSize: 12 }}
                  tickFormatter={(value) => `${value}`}
                  domain={[0, 'dataMax + 100']}
                  tickCount={6}
                  tickMargin={12}
                />

                <ChartTooltip
                  content={<CustomTooltip />}
                  cursor={{
                    stroke: chartConfig.value.color,
                    strokeWidth: 1,
                    strokeDasharray: 'none',
                  }}
                />

                {/* Gradient area */}
                <Area
                  type="linear"
                  dataKey="value"
                  stroke="transparent"
                  fill="url(#salesGradient)"
                  strokeWidth={0}
                  dot={false}
                />

                {/* Main sales line */}
                <Line
                  type="linear"
                  dataKey="value"
                  stroke={chartConfig.value.color}
                  strokeWidth={3}
                  activeDot={{
                    r: 6,
                    fill: chartConfig.value.color,
                    stroke: 'white',
                    strokeWidth: 2,
                    filter: 'url(#dotShadow)',
                  }}
                />
              </ComposedChart>
            </ChartContainer>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
