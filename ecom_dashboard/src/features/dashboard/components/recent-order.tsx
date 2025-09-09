'use client';

import { useEffect, useState } from 'react';
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from '@/shared/components/ui/table';
import { fetchRecentOrders } from '@/features/dashboard/data/dashboard-api';

type Order = {
  id: number;
  customer_name: string;
  product_name: string;
  amount: string;
  status: string;
  date_time: string;
};

export default function RecentOrderTable() {
  const [orders, setOrders] = useState<Order[]>([]);

  useEffect(() => {
    const loadOrders = async () => {
      const data = await fetchRecentOrders();
      setOrders(data);
    };
    loadOrders();
  }, []);

  return (
    <Table>
      <TableCaption>A list of your recent orders.</TableCaption>
      <TableHeader>
        <TableRow>
          <TableHead className="w-[80px]">ID</TableHead>
          <TableHead>Customer</TableHead>
          <TableHead>Product</TableHead>
          <TableHead>Status</TableHead>
          <TableHead>Date</TableHead>
          <TableHead className="text-right">Amount</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {orders.map((order) => (
          <TableRow key={order.id}>
            <TableCell className="font-medium">{order.id}</TableCell>
            <TableCell>{order.customer_name}</TableCell>
            <TableCell>{order.product_name}</TableCell>
            <TableCell>
              <span
                className={`${
                  order.status === 'Completed'
                    ? 'text-green-600'
                    : order.status === 'Pending'
                    ? 'text-yellow-600'
                    : order.status === 'Processing'
                    ? 'text-blue-600'
                    : 'text-red-600'
                }`}
              >
                {order.status}
              </span>
            </TableCell>
            <TableCell>
              {new Date(order.date_time).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
              })}
            </TableCell>
            <TableCell className="text-right">{order.amount}</TableCell>
          </TableRow>
        ))}
      </TableBody>
      <TableFooter>
        <TableRow>
          <TableCell colSpan={5}>Total Revenue</TableCell>
          <TableCell className="text-right">
            {orders
              .reduce((total, order) => total + parseFloat(order.amount.replace(/[^0-9.-]+/g, '')), 0)
              .toLocaleString('en-US', {
                style: 'currency',
                currency: 'USD',
              })}
          </TableCell>
        </TableRow>
      </TableFooter>
    </Table>
  );
}
