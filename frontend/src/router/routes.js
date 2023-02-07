
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'sentient', component: () => import('pages/Index.vue') },
      { path: 'giro', component: () => import('pages/GiroPage.vue') },
      { path: 'admin', component: () => import('pages/AdminPage.vue') },
      { path: 'robo', component: () => import('pages/RoboPage.vue') },
      // { path: 'about', component: () => import('pages/AboutPage.vue') },
      // { path: 'pricing', component: () => import('pages/PricingPage.vue') },
      // { path: 'legal', component: () => import('pages/LegalPage.vue') },
      // { path: 'signup', component: () => import('src/pages/SignUpPage.vue') },
      { path: 'login', component: () => import('src/pages/LoginPage.vue') },
      // { path: 'blackErrorPage', component: () => import('src/pages/blackErrorPage.vue') },
      { path: 'stock', component: () => import('pages/StockPage.vue'),
      children: [
        {path: 'summary', component: () => import('pages/StockSummaryPage.vue')},
        {path: 'charts', component: () => import('pages/StockChartsPage.vue')},
        // {path: 'twitter', component: () => import('pages/StockTwitterPage.vue')},
        // {path: 'financials', component: () => import('pages/StockFinancialsPage.vue'),
        //   children: [
        //     {path: 'incomeStatement', component: () => import('pages/incomeStatement.vue')},
        //     {path: 'balanceSheet', component: () => import('pages/balanceSheet.vue')},
        //     {path: 'cashFlow', component: () => import('pages/cashFlow.vue')},
        //   ]
        // },

        ]

      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
