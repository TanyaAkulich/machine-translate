class UploadedFile < ApplicationRecord
  has_attached_file :file

  validates_attachment_content_type :file, content_type: %w[text/plain text/html text/xml]

  def text
    Nokogiri::HTML(File.open(file.path)).search('p').text.gsub("\n", '').gsub('.', ' ').downcase.gsub(/[[:punct:]]/, '')
  end
end
