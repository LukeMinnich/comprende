const std = @import("std");
const comprende = @import("comprende");

pub fn main() !void {
    // Prints to stderr, ignoring potential errors.
    std.debug.print("All your {s} are belong to us.\n", .{"codebase"});
    try comprende.bufferedPrint();
}

const http = std.http;

test "simple test" {
    const gpa = std.testing.allocator;
    var client = std.http.Client{ .allocator = gpa };
    defer client.deinit();
    const req = try client.fetch(.{
        .method = .GET,
        .location = .{ .url = "https://www.google.com?q=zig" },
    });
    std.debug.print("status={d}\n", .{req.status});
}
