/*
* @File name: itcm
* @Author: Ruige Lee
* @Email: wut.ruigeli@gmail.com
* @Date:   2020-10-29 09:46:49
* @Last Modified by:   Ruige Lee
* @Last Modified time: 2020-10-29 09:52:39
*/



module itcm #
	(
		parameter DW = 32,
		parameter AW = 14,
	)
	(

	input [AW-1:0] addr,
	output [DW-1:0] instr_out,

	input [DW-1:0] instr_in,
	input wen,

	input CLK
	
);


	reg [DW-1:0] ram[0:AW-1];

	always @(posedge CLK) begin
		if(wen) begin
			ram[addr] <= instr_in;
		end else begin
			instr_out <= ram[addr];
		end
	end



endmodule








