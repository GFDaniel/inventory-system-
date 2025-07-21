import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { environment } from "../../environments/environment";
import { InventoryMovement } from "../models/inventory-movement.model";

@Injectable({
  providedIn: "root",
})
export class InventoryMovementService {
  private apiUrl = `${environment.apiUrl}/movements`;

  constructor(private http: HttpClient) {}

  getMovements(productId?: number): Observable<InventoryMovement[]> {
    const url = productId
      ? `${this.apiUrl}/?product_id=${productId}`
      : `${this.apiUrl}/`;
    return this.http.get<InventoryMovement[]>(url);
  }

  createMovement(movement: InventoryMovement): Observable<InventoryMovement> {
    return this.http.post<InventoryMovement>(`${this.apiUrl}/`, movement);
  }
}
