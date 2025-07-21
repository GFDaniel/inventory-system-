export interface InventoryMovement {
  id?: number
  product: number
  product_name?: string
  movement_type: "IN" | "OUT"
  quantity: number
  description: string
  user?: number
  user_name?: string
  created_at?: string
}
