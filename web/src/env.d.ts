import type { readonly } from "astro:schema"

interface ImportMetaEnv {
    readonly SECRET_JWT_KEY: string;
    readonly SECRET_LOGGING_API_KEY: string;
    readonly PASSWORD: string;
    readonly LOGGING_INSTANCE_ID: string;
    readonly LOGGING_URL: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}