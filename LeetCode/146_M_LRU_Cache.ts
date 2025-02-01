class LRUCache {
    capacity: number;
    lruc: Map<number, number>;
    constructor(capacity: number) {
        this.capacity = capacity;
        this.lruc = new Map();
    }
    put(key: number, value: number): void {
        if (this.lruc.has(key)){this.lruc.delete(key);} 
        else if (this.lruc.size >= this.capacity) {
            const firstKey = this.lruc.keys().next().value;
            this.lruc.delete(firstKey);
        }
        this.lruc.set(key, value);
    }
    get(key: number): number {
        if (!this.lruc.has(key)) return -1;
        const value = this.lruc.get(key)!;
        this.lruc.delete(key);
        this.lruc.set(key, value);
        return value;
    }
}