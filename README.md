# E2EE Secure File Sharing System

**Building a more private, secure, and trustworthy way to share files.**

## Overview

E2EE Secure File Sharing is a security-focused file-sharing platform designed to protect files throughout their sharing lifecycle.

Traditional file-sharing systems often require users to trust the service provider with their files, encryption keys, or both. This creates risks involving server-side data exposure, unauthorized access, compromised credentials, insecure key storage, and potential data breaches.

This project aims to address these challenges through an architecture based on **End-to-End Encryption (E2EE), client-side cryptography, secure key management, and zero-knowledge principles.**

The fundamental idea is simple:

**Your files should remain yours. The server should facilitate sharing without needing access to the actual contents of your files.**

## Ultimate Vision

The long-term objective is to develop a robust file-sharing system in which security is considered at every stage — from account creation and file encryption to key exchange, sharing, access control, and file retrieval.

The system aims to achieve:

- **True End-to-End Encryption:** Files are encrypted on the user's device before being uploaded and decrypted only by authorized recipients.
- **Zero-Knowledge Architecture:** The server should never possess the plaintext files, file encryption keys, or users' private encryption keys.
- **Secure Key Management:** Implement a complete key lifecycle covering generation, storage, exchange, rotation, recovery considerations, and revocation.
- **Strong Cryptography:** Use modern, well-established cryptographic algorithms for authenticated file encryption, key exchange, and password-protected private-key storage.
- **Secure Authentication:** Protect accounts and sessions through secure password hashing, session management, cookie security, and appropriate CSRF protection.
- **Integrity and Authenticity:** Detect file tampering and provide mechanisms to verify the authenticity of shared information.
- **Granular Access Control:** Allow users to manage recipients, permissions, and access to shared files.
- **Privacy by Design:** Minimize sensitive metadata exposure and avoid unnecessary collection of user information.
- **Security Against Real-World Threats:** Design, test, and improve the system against attacks such as unauthorized access, session hijacking, CSRF, XSS, man-in-the-middle attacks, key compromise, and server-side data breaches.

## Core Technology Stack

| Component             | Technology              |
| --------------------- | ----------------------- |
| Frontend              | React, TypeScript, Vite |
| Backend               | Python, FastAPI         |
| Database              | PostgreSQL              |
| ORM                   | SQLAlchemy              |
| Password Hashing      | Argon2id                |
| File Encryption       | XChaCha20-Poly1305      |
| Key Exchange          | X25519                  |
| Cryptographic Library | libsodium               |
| Future Object Storage | MinIO                   |

_The cryptographic components are part of the planned architecture and will be implemented and tested incrementally._

## Development Progress

The project is being developed incrementally, with each component tested before moving to the next stage.

### Completed

- [x] Frontend and backend initialization
- [x] FastAPI backend and frontend connectivity
- [x] PostgreSQL database integration
- [x] User registration
- [x] Argon2id password hashing
- [x] User login and password verification
- [x] Secure random session token generation
- [x] Hashed session token storage in the database
- [x] HttpOnly session cookies
- [x] Protected user profile endpoint
- [x] Session expiration and revocation
- [x] Logout functionality

### Planned

- [ ] Client-side file encryption and decryption
- [ ] Public/private key generation and management
- [ ] Secure private-key protection
- [ ] Encrypted file storage
- [ ] Secure key exchange between users
- [ ] Per-file encryption keys and recipient-specific key envelopes
- [ ] File integrity verification
- [ ] Secure file-sharing permissions
- [ ] CSRF protection and additional web security controls
- [ ] Security testing and vulnerability assessment
- [ ] Threat modelling and security documentation
- [ ] Deployment over HTTPS
- [ ] Independent security review

## Security Philosophy

This project is not about claiming that a system is impossible to hack.

It is about building a system where:

1. The server does not need to be trusted with plaintext data.
2. Cryptographic keys are handled with strict separation of responsibilities.
3. Authentication and authorization are independently enforced.
4. Security assumptions are documented and tested.
5. Potential vulnerabilities are treated as engineering problems, not ignored.
6. Security improves continuously through testing, threat modelling, and review.

**The ultimate milestone is not simply to make file sharing work. It is to make privacy and security fundamental properties of how file sharing works.**

## Project Status

🚧 **Under Active Development**

This is an independent cybersecurity project being built to explore applied cryptography, secure backend development, authentication, key management, and practical application security.

The current implementation covers the initial authentication and session-management foundation. End-to-end file encryption and secure key management remain major development milestones.
