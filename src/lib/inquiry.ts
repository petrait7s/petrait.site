/** Demo-request form: options, validation, reference id and mailto fallback. Pure, so it is unit-tested. */

export const businessTypes = [
  "Hotel or resort",
  "Restaurant or café",
  "Distributor or trader",
  "Tour operator or destination organization",
  "Business or shop (website or online store)",
  "Enterprise or large organization",
  "Something else",
] as const;

export const interestOptions = ["PetraPMS", "PetraPOS", "PetraDMS", "Website Build", "E-commerce Build", "Marketing", "Enterprise / custom", "Not sure yet"] as const;

export const limits = { name: 120, company: 160, email: 200, phone: 40, message: 4000 } as const;

export interface InquiryInput {
  name: string;
  email: string;
  phone: string;
  company: string;
  businessType: string;
  interests: string[];
  message: string;
  callDate: string;
}

export type FieldName = keyof InquiryInput;
export type Errors = Partial<Record<FieldName, string>>;

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const DATE = /^\d{4}-\d{2}-\d{2}$/;
const squash = (v: unknown, max: number) => (typeof v === "string" ? v.replace(/\s+/g, " ").trim().slice(0, max) : "");
const keep = (v: unknown, max: number) => (typeof v === "string" ? v.trim().slice(0, max) : "");

export const todayIso = (now = new Date()) => {
  const p = (n: number) => String(n).padStart(2, "0");
  return `${now.getFullYear()}-${p(now.getMonth() + 1)}-${p(now.getDate())}`;
};

export function validateInquiry(raw: Partial<Record<FieldName, unknown>>, now = new Date()): { ok: true; data: InquiryInput } | { ok: false; errors: Errors } {
  const interests = Array.isArray(raw.interests) ? [...new Set(raw.interests.filter((x): x is string => typeof x === "string" && (interestOptions as readonly string[]).includes(x)))] : [];
  const data: InquiryInput = {
    name: squash(raw.name, limits.name),
    email: squash(raw.email, limits.email).toLowerCase(),
    phone: squash(raw.phone, limits.phone),
    company: squash(raw.company, limits.company),
    businessType: typeof raw.businessType === "string" && (businessTypes as readonly string[]).includes(raw.businessType) ? raw.businessType : "",
    interests,
    message: keep(raw.message, limits.message),
    callDate: squash(raw.callDate, 10),
  };
  const errors: Errors = {};
  if (!data.name) errors.name = "Enter your name.";
  if (!EMAIL.test(data.email)) errors.email = "Enter a valid email, like name@company.com.";
  const digits = data.phone.replace(/\D/g, "");
  if (digits.length < 10 || digits.length > 15) errors.phone = "Enter a phone number with 10 to 15 digits.";
  if (!data.businessType) errors.businessType = "Choose the type of business.";
  if (data.message.length < 10) errors.message = "Tell us a little about your operation (at least 10 characters).";
  if (data.callDate) {
    if (!DATE.test(data.callDate) || Number.isNaN(Date.parse(data.callDate))) errors.callDate = "Choose a valid date.";
    else if (data.callDate < todayIso(now)) errors.callDate = "Choose today or a later date.";
  }
  return Object.keys(errors).length ? { ok: false, errors } : { ok: true, data };
}

/** Reference the visitor can quote: INQ-YYMMDD-XXXX (no look-alike letters). */
export function makeRef(now = new Date(), rand: () => number = Math.random): string {
  const letters = "ABCDEFGHJKLMNPQRSTUVWXYZ";
  const p = (n: number) => String(n).padStart(2, "0");
  const code = Array.from({ length: 4 }, () => letters[Math.floor(rand() * letters.length)]).join("");
  return `INQ-${String(now.getFullYear()).slice(2)}${p(now.getMonth() + 1)}${p(now.getDate())}-${code}`;
}

export function inquiryText(d: InquiryInput, ref: string): string {
  return [
    `Reference: ${ref}`,
    `Name: ${d.name}`,
    `Company: ${d.company || "-"}`,
    `Email: ${d.email}`,
    `Phone: ${d.phone}`,
    `Business type: ${d.businessType}`,
    `Interested in: ${d.interests.join(", ") || "-"}`,
    `Preferred call date: ${d.callDate || "-"}`,
    "",
    d.message,
  ].join("\n");
}

export function buildMailto(to: string, d: InquiryInput, ref: string): string {
  return `mailto:${to}?subject=${encodeURIComponent(`Demo request (${ref})`)}&body=${encodeURIComponent(inquiryText(d, ref))}`;
}
