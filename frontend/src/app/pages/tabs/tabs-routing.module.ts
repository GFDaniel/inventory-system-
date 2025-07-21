import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { TabsPage } from "./tabs.page";

const routes: Routes = [
  {
    path: "",
    component: TabsPage,
    children: [
      {
        path: "products",
        loadChildren: () =>
          import("../products/products.module").then(
            (m) => m.ProductsPageModule
          ),
      },
      {
        path: "movements",
        loadChildren: () =>
          import("../movements/movements.module").then(
            (m) => m.MovementsPageModule
          ),
      },
      {
        path: "profile",
        loadChildren: () =>
          import("../profile/profile.module").then((m) => m.ProfilePageModule),
      },
      {
        path: "",
        redirectTo: "/tabs/products",
        pathMatch: "full",
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TabsPageRoutingModule {}
