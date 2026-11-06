import { describe, expect, it } from "vitest";
import { MIN_FPS, chooseTier, downgrade, isTooSlow, type Env } from "../../src/three/tier";

const desktop: Env = { width: 1440, reducedMotion: false, saveData: false, webgl: true, cores: 8, memoryGb: 8, coarsePointer: false };
const tier = (o: Partial<Env>) => chooseTier({ ...desktop, ...o });

describe("chooseTier", () => {
  it("gives a capable desktop the full scene", () => expect(tier({})).toBe("high"));
  it("turns 3D off without WebGL", () => expect(tier({ webgl: false })).toBe("off"));
  it("turns 3D off for reduced motion", () => expect(tier({ reducedMotion: true })).toBe("off"));
  it("turns 3D off for Save-Data", () => expect(tier({ saveData: true })).toBe("off"));
  it("uses the reduced scene on phones (iPhone 16 is 393 wide)", () => expect(tier({ width: 393, coarsePointer: true })).toBe("low"));
  it("uses the reduced scene on touch tablets", () => expect(tier({ width: 820, coarsePointer: true })).toBe("low"));
  it("keeps the full scene on touch laptops", () => expect(tier({ width: 1280, coarsePointer: true })).toBe("high"));
  it("uses the reduced scene on weak CPUs or low memory", () => {
    expect(tier({ cores: 4 })).toBe("low");
    expect(tier({ memoryGb: 4 })).toBe("low");
  });
  it("lets off win over everything else", () => expect(tier({ width: 393, reducedMotion: true })).toBe("off"));
});

describe("downgrade", () => {
  it("steps high to low to off", () => {
    expect(downgrade("high")).toBe("low");
    expect(downgrade("low")).toBe("off");
    expect(downgrade("off")).toBe("off");
  });
});

describe("isTooSlow", () => {
  it("flags frame rates under the minimum", () => expect(isTooSlow(60, 3)).toBe(true));
  it("accepts frame rates at or above the minimum", () => {
    expect(isTooSlow(MIN_FPS, 1)).toBe(false);
    expect(isTooSlow(75, 1.25)).toBe(false);
  });
  it("ignores an empty measurement", () => expect(isTooSlow(0, 0)).toBe(false));
});
