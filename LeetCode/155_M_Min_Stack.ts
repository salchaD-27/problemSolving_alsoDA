class MinStack {
    stack: number[];
    ptr: number;
    constructor() {
        this.stack = [];
        this.ptr = -1;
    }
    push(val: number): void {this.stack[++this.ptr] = val;}
    pop(): void {if (this.ptr >= 0) this.ptr--;}
    top(): number {return this.ptr >= 0 ? this.stack[this.ptr] : -1;}
    getMin(): number {
        if (this.ptr < 0) return -1;
        let min: number = this.stack[0];
        for (let i = 1; i <= this.ptr; i++) {min = min < this.stack[i] ? min : this.stack[i];}
        return min;
    }
}