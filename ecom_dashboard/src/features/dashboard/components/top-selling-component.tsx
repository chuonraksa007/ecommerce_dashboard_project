'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { Badge } from '@/shared/components/ui/badge';
import { Button } from '@/shared/components/ui/button';
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardHeading,
  CardTitle,
  CardToolbar,
} from '@/shared/components/ui/card';
import { Settings } from 'lucide-react';
import { fetchTopSellingProducts } from '@/features/dashboard/data/dashboard-api';

type TopProduct = {
  id: number;
  name: string;
  category: number;
  sales: string;
  units: string;
  trend: string;
  image: string;
};

export default function TopSellingProduct() {
  const [products, setProducts] = useState<TopProduct[]>([]);

  useEffect(() => {
    const loadProducts = async () => {
      const data = await fetchTopSellingProducts();
      setProducts(data);
    };
    loadProducts();
  }, []);

  return (
    <Card className="w-full h-119 lg:max-w-2xl">
      <CardHeader>
        <CardHeading>
          <CardTitle>Top Selling Products</CardTitle>
        </CardHeading>
        <CardToolbar>
          <Button mode="icon" variant="outline" size="sm">
            <Settings />
          </Button>
        </CardToolbar>
      </CardHeader>
      <CardContent className="py-1">
        {products.map((product) => (
          <div
            key={product.id}
            className="flex items-center justify-between gap-2 py-2 border-b border-dashed last:border-none"
          >
            {/* Left: Emoji + Info */}
            <div className="flex items-center gap-3">
              <span className="text-xl">{product.image}</span>
              <div>
                <Link href="#" className="text-sm font-medium text-foreground hover:text-primary">
                  {product.name}
                </Link>
                <div className="text-sm text-muted-foreground">
                  {product.units} • {product.sales}
                </div>
              </div>
            </div>
            {/* Right: Sales trend */}
            <Badge
              appearance="light"
              variant={product.trend.startsWith('+') ? 'primary' : 'destructive'}
            >
              {product.trend}
            </Badge>
          </div>
        ))}
      </CardContent>
      <CardFooter className="justify-center">
        <Button mode="link" underlined="dashed">
          <Link href="#">Learn more</Link>
        </Button>
      </CardFooter>
    </Card>
  );
}
