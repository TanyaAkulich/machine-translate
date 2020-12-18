class TranslateController < ApplicationController
  def index; end

  def upload_file
    file = UploadedFile.create(
      file: params.require(:upload)[:datafile].tempfile,
      file_name: params.require(:upload)[:datafile].original_filename
    )

    @translate = []
    (file.text.size / 500.0).ceil.times do |time|
      part = file.text[time * 500, (time + 1) * 500]
      @translate << JSON.parse(HTTParty.get(URI.escape("http://mymemory.translated.net/api/get?q=#{part}&langpair=en|de")).body)['responseData']['translatedText']
    end

    @translate.join(' ')
    render :index
  end
end
