import jwt from "jsonwebtoken";

const JWT_SECRET = import.meta.env.SECRET_JWT_KEY

export function isAuthenticated(token: string | undefined): boolean {
    if (!token) {
        return false;
    }

    try {
        jwt.verify(token, JWT_SECRET);
        return true
    } catch {
        return false;
    }
}