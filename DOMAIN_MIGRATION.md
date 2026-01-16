# Migration Guide: Render to Vercel for `sgdportfolio.dpdns.org`

Follow these steps to successfully point your domain to your new Vercel deployment.

## Phase 1: Clean up Render (Important)
Before adding the domain to Vercel, it is best to remove it from Render to prevent any SSL certificate conflicts or routing issues.

1.  Log in to your **Render Dashboard**.
2.  Go to your project/web service.
3.  Navigate to the **Settings** tab.
4.  Scroll down to **Custom Domains**.
5.  Click the **Edit** or **Delete** icon next to `sgdportfolio.dpdns.org` to remove it.
    *   *Note: If you plan to delete the entire Render service, that works too.*

## Phase 2: Add Domain to Vercel
1.  Log in to your **Vercel Dashboard**.
2.  Click on your **Portfolio** project.
3.  Go to **Settings** > **Domains**.
4.  Enter `sgdportfolio.dpdns.org` in the input field.
5.  Click **Add**.

## Phase 3: Update DNS Records
Since `sgdportfolio.dpdns.org` is a subdomain, Vercel will likely ask you to configure a **CNAME** record.

1.  Log in to your DNS Provider (where you manage `dpdns.org` or your specific subdomain settings).
2.  Find the DNS records for `sgdportfolio`.
3.  **Delete** any existing A or CNAME records that point to Render (e.g., pointing to `onrender.com` or a Render IP).
4.  **Add/Edit** the record with the values provided by Vercel:

    | Type  | Name (Host) | Value (Target)        | TTL (optional) |
    | :--- | :--- | :--- | :--- |
    | **CNAME** | `@` (or leave blank if it already includes `sgdportfolio`) | `cname.vercel-dns.com` | 3600 |

    *Note: If your provider does not support CNAME on the root of your subdomain (rare), use an **A Record** pointing to `76.76.21.21`.*

## Phase 4: Verification
1.  Go back to the Vercel Domains dashboard.
2.  Vercel will attempt to verify the DNS record. This can take anywhere from a few minutes to 24 hours (depending on DNS propagation), but it is usually fast.
3.  Once verified, Vercel will automatically generate a valid SSL certificate.
4.  Visit [https://sgdportfolio.dpdns.org](https://sgdportfolio.dpdns.org) to check your site.

## Troubleshooting
*   **Invalid Configuration Error**: If you see this in Vercel, double-check that you removed the old records pointing to Render.
*   **SSL Pending**: If it stays stuck on "Generating SSL" for more than an hour, try removing the domain from Vercel and adding it again.
