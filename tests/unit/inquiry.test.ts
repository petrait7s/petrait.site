import { describe, expect, it } from "vitest";
import { buildMailto, inquiryText, makeRef, todayIso, validateInquiry } from "../../src/lib/inquiry";

const now = new Date("2026-11-06T10:00:00");
const good = {
  name: "  Anika   Rahman ",
  email: "Anika@Example.COM ",
  phone: "01712-345678",
  company: "Sea Breeze",
  businessType: "Hotel or resort",
  interests: ["PetraPMS", "PetraPOS", "PetraPMS", "bogus"],
  message: "We run a 60 room resort with two outlets.",
  callDate: "2026-11-10",
};

describe("validateInquiry", () => {
  it("accepts a good request and cleans it", () => {
    const r = validateInquiry(good, now);
    expect(r.ok).toBe(true);
    if (r.ok) {
      expect(r.data.name).toBe("Anika Rahman");
      expect(r.data.email).toBe("anika@example.com");
      expect(r.data.interests).toEqual(["PetraPMS", "PetraPOS"]);
    }
  });
  it("accepts a request without the optional fields", () => {
    expect(validateInquiry({ ...good, company: "", interests: [], callDate: "" }, now).ok).toBe(true);
  });
  it("rejects missing or bad required fields", () => {
    const r = validateInquiry({ name: "", email: "nope", phone: "123", businessType: "x", message: "short", interests: [], callDate: "" }, now);
    expect(r.ok).toBe(false);
    if (!r.ok) expect(Object.keys(r.errors).sort()).toEqual(["businessType", "email", "message", "name", "phone"]);
  });
  it("rejects a past call date and a malformed one", () => {
    const past = validateInquiry({ ...good, callDate: "2026-11-05" }, now);
    expect(past.ok).toBe(false);
    const bad = validateInquiry({ ...good, callDate: "11/10/2026" }, now);
    expect(bad.ok).toBe(false);
  });
  it("accepts today as a call date", () => expect(validateInquiry({ ...good, callDate: todayIso(now) }, now).ok).toBe(true));
  it("caps field lengths", () => {
    const r = validateInquiry({ ...good, name: "a".repeat(500), message: "b".repeat(9000) }, now);
    expect(r.ok).toBe(true);
    if (r.ok) {
      expect(r.data.name.length).toBe(120);
      expect(r.data.message.length).toBe(4000);
    }
  });
  it("ignores non-string input safely", () => {
    const r = validateInquiry({ name: 5, email: {}, phone: null, businessType: [], message: undefined, interests: "PetraPMS", callDate: 1 }, now);
    expect(r.ok).toBe(false);
  });
});

describe("makeRef", () => {
  it("looks like INQ-YYMMDD-XXXX", () => expect(makeRef(now, () => 0)).toBe("INQ-261106-AAAA"));
  it("only uses unambiguous letters", () => expect(makeRef(now, () => 0.99)).toMatch(/^INQ-261106-[A-HJ-NP-Z]{4}$/));
});

describe("mailto fallback", () => {
  const r = validateInquiry(good, now);
  it("addresses the company and carries every field", () => {
    if (!r.ok) throw new Error("fixture invalid");
    const url = buildMailto("petraitbd@gmail.com", r.data, "INQ-261106-ABCD");
    expect(url.startsWith("mailto:petraitbd@gmail.com?subject=")).toBe(true);
    const body = decodeURIComponent(url.split("&body=")[1]);
    expect(body).toBe(inquiryText(r.data, "INQ-261106-ABCD"));
    expect(body).toContain("INQ-261106-ABCD");
    expect(body).toContain("01712-345678");
    expect(body).toContain("We run a 60 room resort");
  });
});
