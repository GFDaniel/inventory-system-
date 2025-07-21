import { NgModule } from "@angular/core"
import { CommonModule } from "@angular/common"
import { ReactiveFormsModule } from "@angular/forms"
import { IonicModule } from "@ionic/angular"
import { MovementsPageRoutingModule } from "./movements-routing.module"
import { MovementsPage } from "./movements.page"

@NgModule({
  imports: [CommonModule, ReactiveFormsModule, IonicModule, MovementsPageRoutingModule],
  declarations: [MovementsPage],
})
export class MovementsPageModule {}
